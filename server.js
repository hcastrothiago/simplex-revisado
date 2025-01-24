import express, { json, urlencoded, static as expressStatic } from 'express';
import axios from 'axios';
import { engine } from 'express-handlebars';
const app = express();
import { join } from 'path';


//handlebars
app.engine('handlebars', engine());
app.set('view engine', 'handlebars')
app.set('views', './views');

//body parser
app.use(json());
app.use(urlencoded({ extended: true }));

//path
app.use(expressStatic(join(__dirname, './public')))

const PORT = process.env.PORT || 3000;

const apiUrl = "http://127.0.0.1:5000"

app.get('/', (req, res) => {
    res.render('home', { isHome: true })
})

// Inicia o servidor
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});

