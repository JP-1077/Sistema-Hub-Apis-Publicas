from backend.app import criacao_banco_dados

app = criacao_banco_dados()

if __name__ == "__main__":
    app.run(debug=True)