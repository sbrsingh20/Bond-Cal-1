import json

def handler(request):
    try:
        # Read request body (if any)
        data = request.json()
        
        # Parameters
        face_value = data.get('face_value', 1000)
        coupon_rate = data.get('coupon_rate', 0.05)
        ytm = data.get('ytm', 0.04)
        years_to_maturity = data.get('years_to_maturity', 10)
        
        # Bond price calculation logic
        coupon_payment = face_value * coupon_rate
        coupon_pv = sum([coupon_payment / (1 + ytm)**t for t in range(1, years_to_maturity + 1)])
        face_value_pv = face_value / (1 + ytm)**years_to_maturity
        bond_price = coupon_pv + face_value_pv
        
        # Return the result as a JSON response
        return {
            'statusCode': 200,
            'body': json.dumps({'bond_price': round(bond_price, 2)})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
