import java.io.*;
class Main {
    static class No {
        protected char conteudo;
        protected No esq;
        protected No right;

        public No(char conteudo){
            this.conteudo = conteudo;
            esq = null;
            right = null;
        }
    }

    static class Arvore{
        protected No raiz;
        protected No aux;
        protected int index = 0;

        public Arvore() {
            raiz = null;
        }


        public void insert(char c[]) {
            No newNo = new No(c[index]);
            raiz = newNo;

            if(c[index] == 'n') {
                newNo.esq = novaFolha(raiz, c[++index], c);
                newNo.right = novaFolha(raiz, c[++index], c);
            }

        }

        public No novaFolha(No parent, char conteudo, char c[]) {
            No aux = new No(conteudo);

            if(conteudo == 'n') {
                aux.esq = novaFolha(aux,c[++index], c);
                aux.right = novaFolha(aux, c[++index], c);
            }
            return aux;
        }

        public int getProf(No n) {
            if(n.conteudo == 'l') {
                return 0;
            }

            int esqProf = getProf(n.esq);
            int rightProf = getProf(n.right);

            if(esqProf> rightProf) {
                return ++esqProf;
            }

            else {
                return ++rightProf;
            }
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        int qtd = Integer.parseInt(in.readLine());
        int saida[] = new int[qtd];

        for(int i = 0; i < qtd; i++) {
            String aux = in.readLine();
            char letters[] = aux.toCharArray();
            Arvore t = new Arvore();
            t.insert(letters);
            saida[i] = t.getProf(t.raiz);
        }

        for(int i = 0; i< qtd; i++) {
            System.out.println(saida[i]);
        }
    }
}
