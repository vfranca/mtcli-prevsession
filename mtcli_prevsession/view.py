"""
View em texto puro, acessível a leitores de tela.
Sem tabelas visuais ou formatação gráfica complexa.
"""

from .model import SessionPrices


class PrevSessionTextView:
    def render(
        self,
        symbol: str,
        prices: SessionPrices,
        variations: list[dict[str, float]],
    ) -> None:
        print(f"Ativo: {symbol}")
        print("-" * 60)
        print("Pregão anterior:")
        print(f"Preço de ajuste:     {prices.ajuste:.2f}")
        print(f"Preço de fechamento:{prices.fechamento:.2f}")
        print(f"VWAP do dia:         {prices.vwap:.2f}")
        print(f"Preço mínimo:        {prices.minimo:.2f}")
        print(f"Preço máximo:        {prices.maximo:.2f}")
        print("-" * 60)
        print("Pregão atual:")
        print(f"Preço de abertura:   {prices.abertura_atual:.2f}")
        print("-" * 60)
        print("Variações percentuais em relação ao ajuste:")
        for v in variations:
            print(
                f"{v['percent']:.1f}% acima: {v['alta']:.2f} | "
                f"{v['percent']:.1f}% abaixo: {v['baixa']:.2f}"
            )
