package learn.avinash.wiki;

import info.bliki.api.Page;
import info.bliki.api.User;
import info.bliki.wiki.filter.SectionHeader;
import info.bliki.wiki.model.ITableOfContent;
import info.bliki.wiki.model.Reference;
import info.bliki.wiki.model.WikiModel;

import java.io.IOException;
import java.util.List;
import static java.lang.System.out;

public class BlikiExample {

    public static void main(String[] args) throws IOException {
        String title = "Wiki software";
        User user = new User("", "", "https://en.wikipedia.org/w/api.php");
        user.login();

        String[] titles = {title};
        List<Page> pages = user.queryContent(titles);

        for (Page page : pages) {
            WikiModel wikiModel = new WikiModel("${image}", "${title}");
            String text = wikiModel.render(page.toString());
            out.println(text);

            out.println("---References---");

            List<Reference> references = wikiModel.getReferences();

            if (references != null) {
                for (Reference reference : references) {
                    out.println(reference.getRefString());
                }
            }


            out.println("---Section Headers---");
            ITableOfContent toc = wikiModel.getTableOfContent();
if(toc!=null){
            List<SectionHeader> sections = toc.getSectionHeaders();
            for (SectionHeader sectionHeader : sections) {
                out.println(sectionHeader.getFirst());
            }

        }
        }
    }
}
