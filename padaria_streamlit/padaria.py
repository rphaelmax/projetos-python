
import streamlit as st

st.set_page_config(page_title="Padaria", page_icon="🥖")

st.title("🥖 Padaria Pão Quentinho")
st.write("Selecione os produtos e suas quantidades.")

produtos = {
    "Pão francês": 1.00,
    "Pão de queijo": 3.50,
    "Croissant": 7.00,
    "Bolo (fatia)": 6.00,
    "Café": 4.00,
    "Leite": 3.50,
    "Suco natural": 8.00,
    "Sanduíche": 12.00
}

st.subheader("Cardápio")

carrinho = {}
total = 0

for produto, preco in produtos.items():
    quantidade = st.number_input(
        f"{produto} - R$ {preco:.2f}",
        min_value=0,
        step=1,
        key=produto
    )

    if quantidade > 0:
        subtotal = quantidade * preco
        carrinho[produto] = (quantidade, subtotal)
        total += subtotal

st.divider()
st.subheader("🛒 Resumo do pedido")

if carrinho:
    for produto, (quantidade, subtotal) in carrinho.items():
        st.write(
            f"{produto} ({quantidade}x) - R$ {subtotal:.2f}"
        )

    st.success(f"Total da compra: R$ {total:.2f}")

    if st.button("Finalizar pedido"):
        st.balloons()
        st.success("Pedido realizado com sucesso!")
else:
    st.info("Selecione pelo menos um produto.")
