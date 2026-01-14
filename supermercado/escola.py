class aluno: 
    def __int__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
    def __str__(self):
        return f"aluno: {self.nome} | matrícula:{self.matricula}"
    
class disciplina: 
    def __int__(self, nome, nota):
        self.nome = nome 
        self.nota = nota
        
    def __str__(self):
        return f"diciplina: {self.nome} | nota:{self.nota}"
    
class historico:
    def __int__(self, nome, periodo):
        self.aluno = aluno
        self.periodo = periodo
        self.disciplina = []
    
    def adicionar_diciplina(self, disciplina):
        self.disciplina.append(disciplina)
        
    def calcular_media(self):
        
    
    
    
    
    