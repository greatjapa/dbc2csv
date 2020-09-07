# dbc2csv [![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/greatjapa/dbc2csv/blob/master/LICENSE)

`dbc2csv` é um utilitário que converte arquivos no formato `dbc` para `csv`. A ideia principal do `dbc2csv` é facilitar pesquisas relacionadas a dados públicos de saúde através da geração de dados em formatos fáceis de serem processados, como `csv`.

*NOTA:* O arquivo `dbc` em questão é um formato proprietário do Departamento de Informatica do SUS (DATASUS) e não possui relação com o formato de mesmo nome da Microsoft FoxPro ou CANdb.

## Como instalar?

Para usar o `dbc2csv` é preciso ter os seguintes programas instalados na sua máquina:
- git
- [docker](https://store.docker.com/editions/community/docker-ce-server-ubuntu)

Logo em seguinda execute os passos abaixo:

```bash
$ git clone https://github.com/greatjapa/dbc2csv.git
$ cd dbc2csv
$ docker build -t dbc2csv .
```

Ao final deste processo teremos uma imagem Docker com todos os programas utlizados na manipulação de arquivos `dbc`.

## Como converter?

Crie uma pasta que contêm os arquivos `dbc` que deseja converter como no exemplo abaixo:
```
source/
    file00.dbc
    file01.dbc
    file02.dbc
    ...
```

Agora execute o comando abaixo passando o caminho completo para o diretório `source`.

```bash
$ docker run -it -v <caminho_completo_para_diretorio_source>:/usr/src/app/data dbc2csv make
```

Ao final do processo, o diretório `source` será preenchido com arquivos `dbf` e `csv`:

```
source/
    file00.dbc
    file00.dbf
    file01.dbc
    file01.dbf
    file02.dbc
    file02.dbf
    csv/
        file00.csv
        file01.csv
        file02.csv
        ...
    ...
```

## Agradecimentos

- A [Prof. Rita Berardi](mailto:ritaberardi@utfpr.edu.br) pela atenção dedicada no desenvolvimento desta ferramenta.
- A toda comunidade que se preocupa com o desenvolvimento e transparência dos dados públicos.

## Referências

* ["Microdatasus: pacote para download e pré-processamento de microdados do Departamento de Informática do SUS (DATASUS)"](https://doi.org/10.1590/0102-311x00032419), `urn:doi:10.1590/0102-311x00032419`.

* [Documentação oficial do SUS](http://cnes.datasus.gov.br/pages/downloads/documentacao.jsp), `http://CNES.DataSUS.gov.br`.



  

