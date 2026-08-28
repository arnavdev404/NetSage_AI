path = r'C:\Users\anand\OneDrive\Desktop\NetSage_AI\dashboard\index.html'
with open(path, encoding='utf-8') as f:
    html = f.read()

idx = html.find('async function drawAllCharts()')
if idx != -1:
    end = html.find('function renderFAQList()', idx)
    print(html[idx:end])
