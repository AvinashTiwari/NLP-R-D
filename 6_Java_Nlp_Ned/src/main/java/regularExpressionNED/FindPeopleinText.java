package regularExpressionNED;

import opennlp.tools.namefind.NameFinderME;
import opennlp.tools.namefind.TokenNameFinderModel;
import opennlp.tools.tokenize.Tokenizer;
import opennlp.tools.tokenize.TokenizerME;
import opennlp.tools.tokenize.TokenizerModel;
import opennlp.tools.util.Span;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

import static java.lang.System.out;

public class FindPeopleinText {

    static final String[] SENTENCES = {"Jack was taller than Peter. ",
            "However, Mr. Smith was taller than both of them. ",
            "The same could be said for Mary and Tommy. ",
            "Mary Anne was the tallest."};

    public static void main(String[] args) {
        openNLPNERExample();
    }

    private static void openNLPNERExample() {
        out.println("---OpenNLP NER Example---");
        try (InputStream tokenModelStream = new FileInputStream(
                new File("E:\\Nlp\\6_Java_Nlp_Ned\\src\\main\\resources\\en-token.bin"));
             InputStream nerModelInputStream = new FileInputStream(
                     new File("E:\\Nlp\\6_Java_Nlp_Ned\\src\\main\\resources\\en-ner-person.bin"));) {

            TokenizerModel tokenizerModel = new TokenizerModel(tokenModelStream);
            Tokenizer tokenizer = new TokenizerME(tokenizerModel);

            TokenNameFinderModel nameModel
                    = new TokenNameFinderModel(nerModelInputStream);
            NameFinderME nameFinder = new NameFinderME(nameModel);

            for (String sentence : SENTENCES) {
                out.println("Sentence: [" + sentence + "]");
                String tokens[] = tokenizer.tokenize(sentence);
                Span nameSpans[] = nameFinder.find(tokens);
                double[] spanProbabilities = nameFinder.probs(nameSpans);

                for (int i = 0; i < nameSpans.length; i++) {
                    out.println("Span: " + nameSpans[i].toString());
                    if ((nameSpans[i].getEnd() - nameSpans[i].getStart()) == 1) {
                        out.println("Entity: "
                                + tokens[nameSpans[i].getStart()]);
                    } else {
                        out.println("Entity: "
                                + tokens[nameSpans[i].getStart()] + " "
                                + tokens[nameSpans[i].getEnd() - 1]);
                    }
                    out.println("Probability: " + spanProbabilities[i]);
                }
                out.println();
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

}
