location /static/ {
    alias /boyuk_qayidish/static/;
}

location /media/ {
    alias /boyuk_qayidish/media/;
}
