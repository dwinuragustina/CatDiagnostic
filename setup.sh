echo '[general]' >> .streamlit/credentials.toml
echo 'email = "int.halim@gmail.com"' >> .streamlit/credentials.toml

echo '' >> .streamlit/config.toml
echo '' >> .streamlit/config.toml
echo '[server]' >> .streamlit/config.toml
echo 'headless = true' >> .streamlit/config.toml
echo 'maxUploadSize = 50' >> .streamlit/config.toml
echo 'enableCORS=false' >> .streamlit/config.toml
echo "port= $PORT" >> .streamlit/config.toml