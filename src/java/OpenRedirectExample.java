// open_redirect.java
import javax.servlet.http.*;
import java.io.IOException;

public class OpenRedirectExample extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String redirectUrl = request.getParameter("url");
        response.sendRedirect(redirectUrl); // Vulnerable to open redirect attacks
    }
}
