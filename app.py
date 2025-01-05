from flask import Flask, render_template, request, make_response
from playwright.sync_api import sync_playwright
import pandas as pd
from io import StringIO
import io

app = Flask(__name__)

# Função para extrair a tabela de FIIs
def extrair_tabela_fiis():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://www.fundsexplorer.com.br/ranking", timeout=10)
        except:
            print("Para os casos de erro de carregamento da pagina")
        
        # Aguarda o iframe específico aparecer
        iframe_selector = 'iframe[src="https://sunoresearch-com-br-7171354.hs-sites.com/hs-web-interactive-7171354-168761900627"]'
        page.wait_for_selector(iframe_selector, timeout=60000)  # Timeout ajustável
        
        page.keyboard.press("Escape")
        
        # Clicar para abrir o seletor de colunas
        page.click(r"#colunas-ranking__select-button")
        
        # Selecionar todos os checkboxes individualmente
        checkboxes = page.locator(".colunas-ranking__selectItem")
        checkboxes.evaluate_all("nodes => nodes.forEach(node => node.checked = true)")
        
        page.wait_for_selector(r'//*[@name="liquidezmediadiaria"]')
        page.click(r'//*[@name="liquidezmediadiaria"]')
        
        page.wait_for_selector(r'//*[@name="tx_performance"]')
        
        #aguardar pelo carregamento da tabela
        page.wait_for_selector("table.default-fiis-table__container__table")
        table_html = page.locator("table.default-fiis-table__container__table").inner_html()
        browser.close()

        df = pd.read_html(StringIO(f"<table>{table_html}</table>"))[0]
        
        print(df.head())
        print(df.columns)
        
        return df

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/atualizar", methods=["GET"])
def atualizar():
    try:
        df = extrair_tabela_fiis()
        tabela_html = df.to_html(classes="table", index=False, border=0)
        return tabela_html
    except Exception as e:
        return f"Erro ao atualizar os dados: {e}", 500

@app.route("/exportar/csv", methods=["GET"])
def exportar_csv():
    try:
        df = extrair_tabela_fiis()
        csv = df.to_csv(index=False, sep=";")
        response = make_response(csv)
        response.headers["Content-Disposition"] = "attachment; filename=fiis.csv"
        response.headers["Content-Type"] = "text/csv"
        return response
    except Exception as e:
        return f"Erro ao exportar CSV: {e}", 500

@app.route("/exportar/xlsx", methods=["GET"])
def exportar_xlsx():
    try:
        df = extrair_tabela_fiis()
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="FIIs")
        response = make_response(output.getvalue())
        response.headers["Content-Disposition"] = "attachment; filename=fiis.xlsx"
        response.headers["Content-Type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        return response
    
    except Exception as e:
        return f"Erro ao exportar XLSX: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)
