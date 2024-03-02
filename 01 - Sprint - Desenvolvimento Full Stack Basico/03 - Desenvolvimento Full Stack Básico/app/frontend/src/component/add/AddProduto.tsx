import { useState } from "react";
import "./AddProduto.style.css"
import { IProduto } from "../../interface/produto/Produto.type";

type Props = {
    onVoltarBtnClick: () => void;
    onSubmitProduto: (data: IProduto) => void;
}


const AddProduto = (props: Props) => {

    const [nome, setNome] = useState("");
    const [quantidade, setQuantidade] = useState("");
    const [valor, setValor] = useState("");

    const { onVoltarBtnClick, onSubmitProduto } = props;

    const onNomeChange = (e: any) => {
        setNome(e.target.value)
    }

    const onQuantidadeChange = (e: any) => {
        setQuantidade(e.target.value)
    }

    const onValorChange = (e: any) => {
        setValor(e.target.value)
    }

    const onClickSubmitProduto = async (e: any) => {
        e.preventDefault();

        const data: IProduto = {
            nome: nome,
            quantidade: parseInt(quantidade),
            valor: parseInt(valor)
        }
        try {
            const response = await fetch('http://127.0.0.1:5000/produto', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8',
                    'Access-Control-Allow-Origin': '*'
                },
                body: JSON.stringify(data)
            });
    
            if (!response.ok) {
                throw new Error('Erro ao enviar a requisição.');
            }
    
            // Aqui você pode tratar a resposta, se necessário
            const responseData = await response.json();
            console.log('Resposta do servidor:', responseData);
        
            onSubmitProduto(responseData)
        } catch (error: any) {
            console.error('Erro ao enviar a requisição:', error.message);
        }
    }

    return (
        <div>

            <form className="form-container" onSubmit={onClickSubmitProduto}>
                <div>
                    <h3>Cadastrar Produto</h3>
                </div>

                <div>
                    <label>Nome:  </label>
                    <input type="text" value={nome} onChange={onNomeChange} />
                </div>
                <div>
                    <label>Quantidade:   </label>
                    <input type="text" value={quantidade} onChange={onQuantidadeChange} />
                </div>
                <div>
                    <label>Valor:   </label>
                    <input type="text" value={valor} onChange={onValorChange} />
                </div>
                <div>
                    <input type="button" value="Voltar" onClick={onVoltarBtnClick} />
                    <input type="button" value="Salvar" onClick={onClickSubmitProduto}/>
                </div>
            </form>
        </div>
    );
}

export default AddProduto;