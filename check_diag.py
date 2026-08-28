path = r'C:\Users\anand\OneDrive\Desktop\NetSage_AI\dashboard\index.html'
with open(path, encoding='utf-8') as f:
    html = f.read()

idx = html.find('AI Diagnosis Results')
if idx != -1:
    end = html.find('Safety Policy', idx)
    print(html[idx:end])
