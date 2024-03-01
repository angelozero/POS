import { useState } from "react";
import "./Home.style.css"
import { IProduto, ProdutoPageEnum, mockProdutoList } from "../../interface/produto/Produto.type";
import ProdutoList from "../list/ProdutoList";
import AddProduto from "../add/AddProduto";

const Home = () => {

    const [produtosList, setProdutosList] = useState(mockProdutoList as IProduto[]);

    const [showPage, setShowPage] = useState(ProdutoPageEnum.list);

    const onAddProdutoClick = () => {
        setShowPage(ProdutoPageEnum.add)
    }

    const showProdutosListPage = () => {
        setShowPage(ProdutoPageEnum.list)
    }

    return (
        <>
            <article className="article-header">
                <header>
                    <h1>Produto</h1>
                </header>
            </article>

            <section className="section-content">
                {
                    showPage === ProdutoPageEnum.list && (
                        <>
                            <input type="button" value="Adicionar Produto" onClick={onAddProdutoClick} />
                            <ProdutoList list={produtosList} />
                        </>
                    )
                }

                {showPage === ProdutoPageEnum.add && <AddProduto onVoltarBtnClick={showProdutosListPage} />}

            </section>
        </>
    );
};

export default Home;