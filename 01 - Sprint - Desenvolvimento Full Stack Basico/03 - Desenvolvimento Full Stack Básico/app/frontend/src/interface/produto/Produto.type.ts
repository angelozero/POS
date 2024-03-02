export interface IProduto {
    id?: string;
    nome: string;
    quantidade: number;
    valor: number;
}

export const mockProdutoList: IProduto[] = [
    {
        id: "123",
        nome: "teste",
        quantidade: 1,
        valor: 30.00
    }
];

export enum ProdutoPageEnum {
    list,
    add,
}