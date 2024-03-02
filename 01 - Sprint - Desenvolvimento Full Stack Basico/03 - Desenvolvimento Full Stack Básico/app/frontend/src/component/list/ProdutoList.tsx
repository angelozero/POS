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
                <tbody>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Quantidade</th>
                        <th>Valor</th>
                        <th>Ação</th>
                    </tr>
                </tbody>
                {list.map((produto, index) => {
                    return (
                        <tbody>
                            <tr key={index}>
                                <td>{`${produto.id}`}</td>
                                <td>{`${produto.nome}`}</td>
                                <td>{`${produto.quantidade}`}</td>
                                <td>{`${produto.valor}`}</td>
                                <td>
                                    <div key={index}>
                                        <input type="button" value="Info" />
                                        <input type="button" value="Deletar" />
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    )
                })}
            </table>
        </div>
    );
};

export default ProdutoList