import pandas as pd
from playwright.async_api import async_playwright

async def extrair_tabela_fiis():
    async with async_playwright() as p:
        # Inicia o navegador
        browser = await p.chromium.launch(headless=True)  # headless=False para ver o navegador funcionando
        context = await browser.new_context()

        # Abre uma nova página
        page = await context.new_page()

        # Acessa a URL
        url = "https://www.fundsexplorer.com.br/ranking"
        await page.goto(url)

        # Aguarda o carregamento completo da tabela
        await page.wait_for_selector("table.default-fiis-table__container__table")

        # Extrai o conteúdo HTML da tabela
        table_html = await page.locator("table.default-fiis-table__container__table").inner_html()

        # Converte o HTML em um DataFrame
        df = pd.read_html(f"<table>{table_html}</table>")[0]

        # Fecha o navegador
        await browser.close()

        # Retorna o DataFrame
        return df

# Exemplo de uso
if __name__ == "__main__":
    import asyncio

    # Executa a função assíncrona
    tabela_fiis = asyncio.run(extrair_tabela_fiis())

    # Exibe os primeiros registros
    print(tabela_fiis.head())
