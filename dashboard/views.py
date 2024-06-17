# views.py

from django.shortcuts import render
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.io as pio

def dashboard(request):
    # Sample data for the charts using Pandas DataFrame
    df1 = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [10, 14, 12, 15, 13],
        'z': [5, 7, 8, 9, 12]
    })
    df2 = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [16, 5, 11, 9, 16],
        'z': [3, 2, 6, 7, 10]
    })

    # Generate Plotly charts using make_subplots
    complex_chart = create_complex_chart(df1, df2)

    context = {
        'selectview': request.POST.get('selectview', ''),
        'hw_rev': request.POST.get('hw_rev', ''),
        'apk': request.POST.get('apk', ''),
        'kpi': request.POST.get('kpi', ''),
        'bspview': request.POST.get('bspview', ''),
        'complex_chart': complex_chart
    }

    print(f"selectview = {context['selectview']}")
    print(f"hw_rev = {context['hw_rev']}")
    print(f"apk = {context['apk']}")
    print(f"kpi = {context['kpi']}")
    print(f"bspview = {context['bspview']}")

    return render(request, 'dashboard.html', context)

def create_complex_chart(df1, df2):
    fig = make_subplots(rows=2, cols=3, subplot_titles=("Chart 1", "Chart 2", "Chart 3", "Chart 4", "Chart 5", "Chart 6"))

    fig.add_trace(go.Scatter(x=df1['x'], y=df1['y'], mode='lines', name='Chart 1'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df2['x'], y=df2['y'], mode='lines', name='Chart 2'), row=1, col=2)
    fig.add_trace(go.Scatter(x=df1['x'], y=df1['z'], mode='lines', name='Chart 3'), row=1, col=3)
    fig.add_trace(go.Scatter(x=df2['x'], y=df2['z'], mode='lines', name='Chart 4'), row=2, col=1)
    fig.add_trace(go.Scatter(x=df1['y'], y=df1['z'], mode='lines', name='Chart 5'), row=2, col=2)
    fig.add_trace(go.Scatter(x=df2['y'], y=df2['z'], mode='lines', name='Chart 6'), row=2, col=3)

    fig.update_layout(height=600, width=900, title_text="Complex Subplots")

    return pio.to_json(fig)




    # print(f"selectview = {context['selectview']}")
    # print(f"hw_rev = {context['hw_rev']}")
    # print(f"apk = {context['apk']}")
    # print(f"kpi = {context['kpi']}")
    # print(f"bspview = {context['bspview']}")






