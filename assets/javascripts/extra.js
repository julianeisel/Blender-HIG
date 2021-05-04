/* Set "data-md-is-localhost" attribute for CSS to use. */
if (location.hostname === "localhost" || location.hostname === "127.0.0.1") {
    document.createAttribute("data-md-is-localhost")
    document.getElementsByTagName("html")[0].setAttribute("data-md-is-localhost", "true");
}
