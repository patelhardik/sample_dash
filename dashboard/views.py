# views.py
from django.shortcuts import render
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio

def dashboard(request):
    # Sample data for the charts using Pandas DataFrame
    df1 = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [10, 14, 12, 15, 13]
    })
    df2 = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [16, 5, 11, 9, 16]
    })

    # Generate Plotly charts
    chart1 = create_chart(df1, 'Chart 1')
    chart2 = create_chart(df2, 'Chart 2')
    chart3 = create_chart(df1, 'Chart 3')
    chart4 = create_chart(df2, 'Chart 4')
    chart5 = create_chart(df1, 'Chart 5')
    chart6 = create_chart(df2, 'Chart 6')

    context = {
        'selectview': request.POST.get('selectview', ''),
        'hw_rev': request.POST.get('hw_rev', ''),
        'apk': request.POST.get('apk', ''),
        'kpi': request.POST.get('kpi', ''),
        'bspview': request.POST.get('bspview', ''),
        'chart1': chart1,
        'chart2': chart2,
        'chart3': chart3,
        'chart4': chart4,
        'chart5': chart5,
        'chart6': chart6,
    }

    print(f"selectview = {context['selectview']}")
    print(f"hw_rev = {context['hw_rev']}")
    print(f"apk = {context['apk']}")
    print(f"kpi = {context['kpi']}")
    print(f"bspview = {context['bspview']}")

    return render(request, 'dashboard.html', context)

def create_chart(df, title):
    trace = go.Scatter(x=df['x'], y=df['y'], mode='lines', name=title)
    layout = go.Layout(title=title, autosize=True)
    fig = go.Figure(data=[trace], layout=layout)
    return pio.to_json(fig)









