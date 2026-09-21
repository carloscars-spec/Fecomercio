import pandas as pd, re, json
in_file = r'C:\\Users\\Home\\Downloads\\dados brutos.xlsx'
out_file = r'C:\\Users\\Home\\Desktop\\GeckoAi\\Fecomercio\\Fecomércio\\data.json'
df = pd.read_excel(in_file, engine='openpyxl', sheet_name=0)
def val(row, i):
    v = row.iloc[i]
    if pd.isna(v) or str(v).strip() == '':
        return None
    return str(v).strip()
def score(row, i):
    v = val(row, i)
    if not v:
        return 0
    m = re.match(r'^([1-5])', v)
    return int(m.group(1)) if m else 0
records = []
for _, row in df.iterrows():
    records.append(
        {
            'age': val(row, 7),
            'sex': val(row, 8),
            'income': val(row, 9),
            'user': val(row, 64),
            'coexist': val(row, 99),
            'coexistInfluence': val(row, 100),
            'coexistOrder': val(row, 115),
            'freq': val(row, 10),
            'healthy': val(row, 53),
            'attention': val(row, 54),
            'permanent': val(row, 63),
            'portion': val(row, 128),
            'influence': {
                'Saúde': score(row, 56),
                'Controle de peso': score(row, 57),
                'Aparência/corpo': score(row, 58),
                'Atividade física': score(row, 59),
                'Prevenção de doenças': score(row, 60),
                'Disposição/energia': score(row, 61),
                'Bem-estar': score(row, 62),
            },
        }
    )
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False, separators=(',', ':'))
