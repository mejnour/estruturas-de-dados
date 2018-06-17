import java.lang.*;
import java.io.*;

class Main {
    static class No {
        protected int conteudo;
        protected No left;
        protected No right;

        public No(int conteudo) {
            this.conteudo = conteudo;
            left = null;
            right = null;
        }
    }

    static class Arvore {
        protected No raiz;
        protected int C;

        public Arvore() {
            raiz = null;
            C = 0;
        }

        public void insertRaiz(int X) {
            No newNo = new No(X);
            raiz = newNo;
        }

        public void insert(int X, No N) {
            while (true) {
                C++;
                if (X < N.conteudo) {
                    if (N.left == null) {
                        No newNo = new No(X);
                        N.left = newNo;
                        break;
                    }

                    else {
                        N = N.left;
                    }
                }

                else {
                    if (N.right == null) {
                        No newNo = new No(X);
                        N.right = newNo;
                        break;
                    }

                    else {
                        N = N.right;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        Arvore t = new Arvore();

        int length = Integer.parseInt(in.readLine());

        for (int i = 0; i < length; i++) {
            int X = Integer.parseInt(in.readLine());

            if (i == 0) {
                t.insertRaiz(X);
                System.out.println(t.C);
            }

            else {
                t.insert(X, t.raiz);
                System.out.println(t.C);
            }
        }
    }
}
