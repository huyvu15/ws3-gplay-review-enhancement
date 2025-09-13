import json
import requests
import boto3
from datetime import datetime

client = boto3.resource('dynamodb')

def get_current_month_statistics():
    try:
        table = client.Table('Spend-me')
        response = table.scan()
        total_spend = 0
        total_food_spend = 0
        total_fuel_spend = 0
        current_date = datetime.now()
        current_month = current_date.month
        current_year = current_date.year
        
        for item in response['Items']:
            if 'spend' in item and item['spend'].isdigit():
                spend_amount = int(item['spend'])
            else:
                continue
            
            if 'date' in item and '-' in item['date']:
                date = item['date']
                date_parts = date.split('-')
                if len(date_parts) == 3:
                    item_month = int(date_parts[1])
                    item_year = int(date_parts[2])
                    if item_month != current_month or item_year != current_year:
                        continue
            
            total_spend += spend_amount
            
            if 'spend_name' in item:
                spend_name = item['spend_name'].lower()
                if 'ăn' in spend_name:
                    total_food_spend += spend_amount
                elif 'đổ xăng' in spend_name:
                    total_fuel_spend += spend_amount
        
        return total_spend, total_food_spend, total_fuel_spend
    
    except Exception as e:
        print(f"Error in get_current_month_statistics: {e}")
        raise

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        chat_id = body['message']['chat']['id']
        message_text = body['message']['text']
        
        url = "https://api.telegram.org/bot7495737041:AAEaYP_GjeyPjtE09d4LRLth2ZfWRPmUx_4/sendMessage"
        
        if message_text.startswith('/sum'):
            total_spend, total_food_spend, total_fuel_spend = get_current_month_statistics()
            response_text = (f"Đây là thống kê chi tiết chi tiêu tháng này của bạn:\n"
                             f"Tổng chi tiêu: {total_spend}\n"
                             f"Tổng tiền ăn: {total_food_spend}\n"
                             f"Tổng tiền đổ xăng: {total_fuel_spend}")
        
        elif message_text.startswith('/chi'):
            parts = message_text.split('|')
            if len(parts) == 3:
                spend = int(parts[0].strip().split()[1])  # Extract the amount from the command
                spend_name = parts[1].strip()  # Extract the spend name
                date = parts[2].strip()  # Extract the date
                formatted_date = datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')  # Format the date properly
                table = client.Table('Spend-me')
                response = table.put_item(
                    Item={
                        'id': str(datetime.now().timestamp()),
                        'spend': str(spend),
                        'spend_name': spend_name,
                        'date': formatted_date
                    }
                )
                response_text = "Dữ liệu đã ghi vào cơ sở dữ liệu thành công."
            else:
                response_text = "Sai định dạng. Định dạng đúng: /chi 10000 | Mua áo | 12-7-2023"
        elif message_text.startswith('/show'):
            table = client.Table('Spend-me')
            response = table.scan(Limit=5)
            items = response['Items']
            response_text = "Top 5 ghi chép mới nhất:\n"
            for item in items:
                response_text += f"- ID: {item.get('id', 'N/A')}, Spend: {item.get('spend', '0')}, Name: {item.get('spend_name', 'N/A')}, Date: {item.get('date', 'N/A')}\n"
        else:
            response_text = "Lệnh không hợp lệ. Vui lòng sử dụng /chi để nhập chi tiêu hoặc /sum để xem thống kê."
        
        payload = {'chat_id': chat_id, 'text': response_text}
        requests.post(url, json=payload)
        return {"statusCode": 200, "body": json.dumps({"message": "Success"})}
    
    except Exception as e:
        print(f"Error in lambda_handler: {e}")
        return {"statusCode": 500, "body": json.dumps({"message": "Error"})}
