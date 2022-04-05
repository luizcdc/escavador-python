from pathlib import Path


class Documento(object):

    @staticmethod
    def get_pdf(conteudo, path, nome_arquivo):
        """
        Salva um pdf vindo de respostas da API com o nome enviado, no diretório informado
        :param nome_arquivo: nome do arquivo a ser criado
        :param conteudo: pdf vindo de respostas da API
        :param path: caminho onde o pdf será salvo
        :return: json
        """
        real_path = Path(path) / f"{nome_arquivo}.pdf"
        try:
            with open(real_path, "xb+") as arquivo:
                arquivo.write(conteudo)
        except FileExistsError as error:
            return {"error": error.strerror}
        except FileNotFoundError as error:
            return {"error": error.strerror}

        return {"path": real_path}
