import java.io.*;

class Main {
	static class No{
		int data;
		No left;
		No right;

		public No(int data){
      this.data = data;
      left = null;
      right = null;
		}
	}

	static class Arvore{
		protected String posStr = "";
		protected static int preIndex = 0;

		private No monta(String in[], String pre[], int inStrt, int inEnd){
      if (inStrt > inEnd)
        return null;

      int data = Integer.parseInt(pre[preIndex++]);
      No tNo = new No(data);

      if (inStrt == inEnd)
        return tNo;

      int inIndex = search(in, inStrt, inEnd, tNo.data);

      tNo.left = monta(in, pre, inStrt, inIndex - 1);
      tNo.right = monta(in, pre, inIndex + 1, inEnd);

      return tNo;
	    }

		private int search(String vec[], int comeca, int fim, int data){
      int i;
      for (i = comeca; i <= fim; i++){
      	int vecValue = Integer.parseInt(vec[i]);
          if ( vecValue == data)
            return i;
      }
      return i;
    }

		private void posOrdemArvore(No no){
      if (no == null) return;

      posOrdemArvore(no.left);
      posOrdemArvore(no.right);
      posStr += no.data + " ";
    }

		private String equalsStr() {
			return posStr;
		}

	}

	public static void main(String[] args) throws IOException{
    Arvore tree = new Arvore();

    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    int tamanho = Integer.parseInt(in.readLine());

    String pre = in.readLine();
    String preOrdem[] = pre.split(" ");

    String pos = in.readLine();

    String inOr = in.readLine();
    String inOrdem[] = inOr.split(" ");

    No root = tree.monta(inOrdem, preOrdem, 0, tamanho-1);

    tree.posOrdemArvore(root);

    String posArvore = tree.equalsStr();

    String posStr = posArvore.substring(0, posArvore.length() - 1);
    if(pos.equals(posStr)) {
            System.out.println("yes");
    }

    else {
            System.out.println("no");
    }
	}
}
