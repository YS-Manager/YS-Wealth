from twilio.rest import Client
import plotly.graph_objects as go

from .models import Stock, StockSector


def send_sms(request):
    account_sid = 'AC4df7ec37cccef22b3dc88d06496973ea'
    auth_token = '7052666be54946f1d2cb663bb6813919'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                from_= "+13253996109",
                body=f'YS-WEALTH\nusername: {request.user.username}\nMessage: "He is trying to enter wrong otp."',
                to=f"+917838367854",
            )
    


def graph(request):
    sectors = StockSector.objects.all()
    labels = [sector.name for sector in sectors]
    values = [sector.stocks.filter(user=request.user).count() for sector in sectors]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    
    fig.update_traces(textposition='inside', textinfo='percent+label', hoverinfo="label+percent+name")

    fig.update_layout(title_text="Stock Investment")

    chart = fig.to_html()
    return chart