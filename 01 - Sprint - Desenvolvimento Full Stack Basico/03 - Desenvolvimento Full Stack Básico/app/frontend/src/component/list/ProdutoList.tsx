import { IProduto } from "../../interface/produto/Produto.type"
import "./ProdutoList.style.css"

type Props = {
    list: IProduto[];
}

const ProdutoList = (props: Props) => {

    const { list } = props;

    return (
        <div>

            <table>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Quantidade</th>
                    <th>Valor</th>
                    <th>Ação</th>
                </tr>
                {list.map(produto => {
                    return (
                        <tr key={produto.id}>
                            <td>{`${produto.id}`}</td>
                            <td>{`${produto.nome}`}</td>
                            <td>{`${produto.quantidade}`}</td>
                            <td>{`${produto.valor}`}</td>
                            <td>
                                <div>
                                    <input type="button" value="Info" />
                                    <input type="button" value="Deletar" />
                                </div>
                            </td>
                        </tr>
                    )
                })}
            </table>
        </div>
    );
};

export default ProdutoList