import java.io.*;

class Main {

    static class No{
        private int conteudo;
	private No prox;
        private No ant;

	public No(){
            setProx(null);
            setAnt(null);
	}

        public void setConteudo(int conteudo) {
            this.conteudo = conteudo;
	}

	public int getConteudo() {
            return conteudo;
	}

	public void setProx(No prox) {
            this.prox = prox;
	}

	public No getProx() {
            return prox;
	}

        public void setAnt(No ant) {
            this.ant = ant;
        }

        public No getAnt() {
            return ant;
        }
    }

    static class Fila{
        protected No inicio;
        protected No fim;
        protected int numElem;
        protected boolean reversed = false;

        public Fila() {
            inicio = null;
            fim = null;
            numElem = 0;
	}

        public void command(String s){
            String[] cmmd = s.split(" ");

            if(cmmd[0].equals("back")){
                removeBack();
            }
            if(cmmd[0].equals("front")){
                removeFront();
            }
            if(cmmd[0].equals("reverse")){
                reverse();
            }
            if(cmmd[0].equals("push_back")){
                pushBack(cmmd[1]);
            }
            if(cmmd[0].equals("toFront")){
                pushFront(cmmd[1]);
            }
        }

        public void pushFront(String s){
            int data = Integer.parseInt(s);
            No newNo = new No();
            newNo.setConteudo(data);

            if(reversed){
                reverse();
                pushBack(s);
                reverse();
            }

            else{
                if(numElem == 0){
                    inicio = newNo;
                    fim = newNo;
                }

                else{
                    inicio.setAnt(newNo);
                    newNo.setProx(inicio);
                    inicio = newNo;
                }

                numElem++;
            }
        }

        public void pushBack(String s){
            int data = Integer.parseInt(s);
            No newNo = new No();
            newNo.setConteudo(data);

            if(reversed){
                reverse();
                pushFront(s);
                reverse();
            }

            else{
                if(numElem == 0){
                    inicio = newNo;
                }

                else{
                    newNo.setAnt(fim);
                    fim.setProx(newNo);
                }

                fim = newNo;
                numElem++;
            }
        }

        public void removeFront(){

            if(reversed){
                reverse();
                removeBack();
                reverse();
            }

            else{

                if(numElem == 0){
                    System.out.println("No job for Ada?");
                }

                else{
                    int aux = inicio.getConteudo();
                    No p = inicio;

                    if(inicio == fim){
                        inicio = null;
                        fim = null;
                    }

                    else{
                        inicio = p.getProx();
                        p.setProx(null);
                        inicio.setAnt(null);
                    }

                    p = null;
                    numElem--;
                    System.out.println(aux);
                }
            }
        }

        public void removeBack(){

            if(reversed){
                reverse();
                removeFront();
                reverse();
            }

            else{

                if(numElem == 0){
                    System.out.println("No job for Ada?");
                }

                else{
                    int aux = fim.getConteudo();
                    No p = fim;

                    if(inicio == fim){
                        inicio = null;
                        fim = null;
                    }

                    else{
                        fim = p.getAnt();
                        fim.setProx(null);
                    }

                    p = null;
                    numElem--;
                    System.out.println(aux);
                }
            }
        }

        public void reverse(){
           if(numElem == 0) return;

           No aux = inicio;
           inicio = fim;
           fim = aux;
           reversed =  !reversed;

        }
    }

    public static void main(String[] args) throws IOException{


            BufferedReader in = new BufferedReader(
                    new InputStreamReader(System.in));
            Fila queue = new Fila();
            int length = Integer.parseInt(in.readLine());

            for(int i = 0; i < length; i++){
                String a = in.readLine();
                queue.command(a);
            }

    }
}
