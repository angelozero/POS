import "./AddProduto.style.css"

type Props = {
    onVoltarBtnClick: () => void;
}

const AddProduto = (props: Props) => {

    const { onVoltarBtnClick } = props;

    return (
        <div>

            <form className="form-container">
                <div>
                    <h3>Cadastrar Produto</h3>
                </div>

                <div>
                    <label>Nome:  </label>
                    <input type="text" />
                </div>
                <div>
                    <label>Quantidade:   </label>
                    <input type="text" />
                </div>
                <div>
                    <label>Valor:   </label>
                    <input type="text" />
                </div>
                <div>
                    <input type="button" value="Voltar" onClick={onVoltarBtnClick} />
                    <input type="button" value="Salvar" />
                </div>
            </form>
        </div>
    );
}

export default AddProduto;