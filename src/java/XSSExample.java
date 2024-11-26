// xss.java
import javax.servlet.http.*;
import java.io.IOException;

public class XSSExample extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String userInput = request.getParameter("input");
        response.getWriter().println("<html><body>" + userInput + "</body></html>"); // Vulnerable to XSS
    }
}
