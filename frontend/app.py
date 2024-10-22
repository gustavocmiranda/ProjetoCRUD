import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide")
st.title("Gerenciamento de produtos")

def show_response_message(response):
    if response.status_code == 200:
        st.success("Operação realizada com sucesso!")
    else:
        try:
            data = response.json()
            if 'detail' in data:
                if isinstance(data['detail'], list):
                    errors = "\n".join([error['msg'] for error in data['detail']])
                    st.error(f"Erro: {errors}")
                else:
                    st.error(f"Erro: {data['detail']}")
        except ValueError:
            st.error("Erro desconhecido. Não foi possível decodificar a resposta")

with st.expander("Cadastrar produto"):        
    with st.form("Novo produto"):
        name = st.text_input("Nome do produto")
        category = st.selectbox("Categoria do produto",
                                ("Roupas", "Acessórios", "Eletrodomésticos", "Utensílios de cozinha", "Petshop"),
                                index= None,
                                placeholder= "Escolha uma categoria...")
        description = st.text_area("Descrição do produto")
        price = st.number_input("Preço do produto",
                                min_value=0.01,
                                format="%.2f",
                                placeholder="Insira um valor numérico",
                                value=None)
        email_fornecedor = st.text_input("Email do fornecedor do produto", placeholder="exemplo@exemplo.com")

        if st.form_submit_button("Adicionar produto"):
            response = requests.post(
                "http://backend:8000/products/",
                json={
                "name": name,
                "category": category,
                "description": description,
                "price": price,
                "email_fornecedor": email_fornecedor
                }
            )
            show_response_message(response)


            st.write("Produto cadastrado com sucesso!")
            st.write()

with st.expander("Exibir todos os produtos"):
    if st.button("Exibir todos os produtos"):
        response = requests.get("http://backend:8000/products/")
        if response.status_code == 200:
            products = response.json()
            df = pd.DataFrame(products)

            df = df[[
                "id",
                "name",
                "description",
                "price",
                "category",
                "email_fornecedor",
                "created_at"
            ]]

            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

with st.expander("Obter mais detalhes de um produto"):
    product_id = st.number_input("ID do produto", min_value=1, format="%d")
    if st.button("Buscar produto"):
        response = requests.get(f"http://backend:8000/products/{product_id}")
        if response.status_code == 200:
            products = response.json()
            df = pd.DataFrame([products])

            df = df[[
                "id",
                "name",
                "description",
                "price",
                "category",
                "email_fornecedor",
                "created_at"
            ]]

            st.write(df.to_html(index=False), unsafe_allow_html=True)

        else:
            show_response_message(response)

with st.expander("Deletar produto"):
    product_id_delete = st.number_input("ID do produto", min_value=1, format="%d", key=2)
    if st.button("Deletar produto"):
        response = requests.delete(f"http://backend:8000/products/{product_id_delete}")
        show_response_message(response)

with st.expander("Atualizar produto"):
    with st.form("Atualizar"):
        product_id_update = st.number_input("ID do produto", min_value=1, format="%d", key=3)
        new_name = st.text_input("Nome do produto")
        new_category = st.selectbox("Categoria do produto",
                                ("Roupas", "Acessórios", "Eletrodomésticos", "Utensílios de cozinha", "Petshop"),
                                index= None,
                                placeholder= "Escolha uma categoria...")
        new_description = st.text_area("Descrição do produto")
        new_price = st.number_input("Preço do produto",
                                min_value=0.01,
                                format="%.2f",
                                placeholder="Insira um valor numérico",
                                value=None)
        new_email_fornecedor = st.text_input("Email do fornecedor do produto", placeholder="exemplo@exemplo.com")

        if st.form_submit_button("Atualizar produto"):
            update_data = {}
            if new_name:
                update_data['name'] = new_name
            if new_category:
                update_data['category'] = new_category
            if new_description:
                update_data['description'] = new_description
            if new_price:
                update_data['price'] = new_price
            if new_email_fornecedor:
                update_data['email_fornecedor'] = new_email_fornecedor
            
            if update_data:
                response = requests.put(
                    f"http://backend:8000/products/{product_id_update}",
                    json=update_data
                    )
                show_response_message(response)
            else:
                st.error("Nenhuma informação fornecida")
