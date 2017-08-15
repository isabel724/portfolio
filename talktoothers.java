<!DOCTYPE html>
<html> 
 <head>
<title>Talk To Others</title>
</head>
java.lang.ClassCastException: javax.swing.JViewport cannot be cast to javax.swing.JTextPane
    at ChatBox.getTextPane(ChatBox.java:41)
    at ChatBox.getDocument(ChatBox.java:45)
    at ChatBox.addMessage(ChatBox.java:50)
    at ImageTest2.main(ImageTest2.java:160)
 
 public class ChatBox extends JScrollPane {

private Style style;

public ChatBox() {

    StyleContext context = new StyleContext();
    StyledDocument document = new DefaultStyledDocument(context);

    style = context.getStyle(StyleContext.DEFAULT_STYLE);
    StyleConstants.setAlignment(style, StyleConstants.ALIGN_LEFT);
    StyleConstants.setFontSize(style, 14);
    StyleConstants.setSpaceAbove(style, 4);
    StyleConstants.setSpaceBelow(style, 4);

    JTextPane textPane = new JTextPane(document);
    textPane.setEditable(false);

    this.add(textPane);
}

public JTextPane getTextPane() {
    return (JTextPane) this.getComponent(0);
}

public StyledDocument getDocument() {
    return (StyledDocument) getTextPane().getStyledDocument();
}

public void addMessage(String speaker, String message) {
    String combinedMessage = speaker + ": " + message;
    StyledDocument document = getDocument();

    try {
        document.insertString(document.getLength(), combinedMessage, style);
    } catch (BadLocationException badLocationException) {
        System.err.println("Oops");
    }
}
}
</html>
