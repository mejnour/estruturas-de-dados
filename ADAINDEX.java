import java.util.*;

import java.lang.String.*;
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	
	public static class No {
		private No ant;
		private String conteudo;
		private No prox;
		
		public No(){
			setProx(null);
		}

		public String getConteudo() {
			return conteudo;
		}

		public void setConteudo(String conteudo) {
			this.conteudo = conteudo;
		}

		public No getProx() {
			return prox;
		}

		public void setProx(No prox) {
			this.prox = prox;
		}

		public No getAnt() {
			return ant;
		}

		public void setAnt(No ant) {
			this.ant = ant;
		}
	}


	public static class LDE {
		
				
		private No inicio;
		private No fim;
		private int tamanho;
		
		public LDE(){
			inicio = null;
			fim = null;		
			tamanho = 0;
		}
		
		
		public boolean vazia() {
		    if (tamanho == 0)
		        return true;
		    else
		        return false;
		}

		
		public int tamanho() {
		    return tamanho;
		}
		
		private boolean insereInicioLista(String valor) {
			
		    No novoNo = new No();
		    
		    
		    novoNo.setConteudo(valor);
		    novoNo.setProx(inicio);
		    
		    novoNo.setAnt(null); 
		    if (vazia())
	    			fim = novoNo; 
		    else
	    			inicio.setAnt(novoNo); 
		    
		    inicio = novoNo;
		    tamanho++;
		    return true;
		}
		
		
		public String elemento (int pos) {
		    No aux = inicio;
		    int cont = 1;

		
		    while (cont < pos){
		
		        aux = aux.getProx();
		        cont++;
		    }

		    return aux.getConteudo();
		}

		
		private boolean insereMeioLista(int pos, String dado){
		    int cont = 1;

		    
		    No novoNo = new No();
		    novoNo.setConteudo(dado);

		    
		    No aux = inicio;
		    while ((cont < pos-1) && (aux != null)){
		          aux = aux.getProx();
		          cont++;
		    }

		    if (aux == null) {  
		    		return false;
		    }

		    
		    novoNo.setAnt(aux); 
		    novoNo.setProx(aux.getProx());
		    
		    aux.getProx().setAnt(novoNo); 
		    
		    aux.setProx(novoNo);

		    tamanho++;
		    return true;
		}

		
		private boolean insereFimLista(String dado){
		    
		    No novoNo = new No();
		    novoNo.setConteudo(dado);

		    
		    No aux = inicio;
		    while(aux.getProx() != null){
		        aux = aux.getProx();
		    }

		    novoNo.setProx(null);
		    aux.setProx(novoNo);
		    
		    novoNo.setAnt(fim);  
		    fim.setProx(novoNo); 
		    fim = novoNo; 		
		    
		    this.tamanho++;
		    return true;
		}
	}
	
	static Scanner input = new Scanner(System.in);

	public static void main(String[] args) throws IOException{

		LDE lista = new LDE();
		int q, n;
		BufferedReader in = new BufferedReader(
				new InputStreamReader(System.in));
		String a = in.readLine();
        String[] partes = a.split(" ");
        n = Integer.parseInt(partes[0]);
        q = Integer.parseInt(partes[1]);
		for(int i = 0; i < n;  i++){
			if(lista.vazia())
				lista.insereInicioLista(in.readLine());
			else
				lista.insereFimLista(in.readLine());
		}
		
		for(int i = 0; i < q; i++) {
			String querie = in.readLine();
			int count = 0;
			
			for(int j = 1; j <= lista.tamanho; j++) {
				if(lista.elemento(j).startsWith(querie)) {
					count++;
				}
			}
			System.out.println(""+count);
		}
	}
}