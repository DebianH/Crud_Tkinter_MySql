from tkinter import *
from tkinter import ttk
from vender import Vender
from tkinter import messagebox

class Ventana(Frame):
    productos = Vender()

    def __init__(self, master=None):
        super().__init__(master,width=680, height=260)
        self.master = master
        self.pack()
        self.create_widget()
        self.mostrar_data()
        self.habilitarCajas("disabled")
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")
        self.id=-1

    def habilitarCajas(self,estado):
        self.txtCodigo.configure(state=estado)
        self.txtProducto.configure(state=estado)
        self.txtGrupo.configure(state=estado)
        self.txtPrecio.configure(state=estado)
    
    def habilitarBtnOper(self,estado):
        self.btnNuevo.configure(state=estado)
        self.btnmodificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarBtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def limpiarCaja(self):
        self.txtCodigo.delete(0,END)
        self.txtProducto.delete(0,END)
        self.txtGrupo.delete(0,END)
        self.txtPrecio.delete(0,END)

    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def mostrar_data(self):
        datos = self.productos.consulta_productos()
        for row in datos:
            self.grid.insert("", END,text=row[0],values=(row[1],row[2],row[3],row[4],))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])
    def fNuevo(self):
        self.habilitarCajas("normal")
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCaja()
        self.txtCodigo.focus()

    def fGuardar(self):
        if self.id ==-1:
            self.txtCodigo.get()
            self.productos.inserta_productos(self.txtCodigo.get(),self.txtProducto.get(),self.txtGrupo.get(),self.txtPrecio.get())

        else:
            self.productos.editar_productos(self.id,self.txtCodigo.get(),self.txtProducto.get(),self.txtGrupo.get(),self.txtPrecio.get())
            self.id=-1

        self.limpiaGrid()
        self.mostrar_data()
        self.limpiarCaja()
        self.habilitarBtnGuardar('disabled')
        self.habilitarBtnOper('normal')
        self.habilitarCajas("disabled")

    def fModificar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected,'text')
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento!')
        else:
            self.id=clave
            self.habilitarCajas("normal")
            valores = self.grid.item(selected,'values')
            self.txtCodigo.delete(0,END)
            self.txtCodigo.insert(0,valores[0])
            self.txtProducto.insert(0,valores[1])
            self.txtGrupo.insert(0,valores[2])
            self.txtPrecio.insert(0,valores[3])

            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")

            self.txtCodigo.focus()
    
    def fEliminar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected,'text')
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento!')
        else:
            valores = self.grid.item(selected,'values')
            data = str(clave) + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar","Deseas eliminar registro seleccionado?\n" + data)

        if r == messagebox.YES:
            n = self.productos.elimina_productos(clave)
            if n == 1:
                messagebox.showinfo("Eliminar","Elemento eliminado correctamente.")
                self.limpiaGrid()
                self.mostrar_data()
            else:
                messagebox.showwarning("Eliminar","No es posible elimar elemento")


    def fCancelar(self):
        r = messagebox.askquestion("Cancelar","Cancelar operacion?")
        if r == messagebox.YES:
            self.limpiarCaja()
            self.habilitarBtnGuardar("disabled")
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")

    def create_widget(self):
        frame1 = Frame(self, bg="DodgerBlue2")
        frame1.place(x=0,y=0,width=93,height=259)

        self.btnNuevo=Button(frame1,text="Nuevo",command=self.fNuevo,bg="light cyan")
        self.btnNuevo.place(x=5,y=50,width=80,height=30)

        self.btnmodificar=Button(frame1,text="Editar",command=self.fModificar,bg="light cyan")
        self.btnmodificar.place(x=5,y=90,width=80,height=30)
        
        self.btnEliminar=Button(frame1,text="Eliminar",command=self.fEliminar,bg="light cyan")
        self.btnEliminar.place(x=5,y=130,width=80,height=30)

        frame2 = Frame(self, bg="#d3dde3")
        frame2.place(x=95,y=0,width=150,height=259)

        lbl1 = Label(frame2,text="Codigo")
        lbl1.place(x=3,y=5)
        self.txtCodigo=Entry(frame2)
        self.txtCodigo.place(x=3,y=25,width=50,height=20)

        lbl2 = Label(frame2,text="Producto")
        lbl2.place(x=3,y=55)
        self.txtProducto=Entry(frame2)
        self.txtProducto.place(x=3,y=75,width=100,height=20)
        
        lbl3 = Label(frame2,text="Grupo")
        lbl3.place(x=3,y=105)
        self.txtGrupo=Entry(frame2)
        self.txtGrupo.place(x=3,y=125,width=100,height=20)

        lbl4 = Label(frame2,text="Precio")
        lbl4.place(x=3,y=155)
        self.txtPrecio=Entry(frame2)
        self.txtPrecio.place(x=3,y=175,width=100,height=20)

        self.btnGuardar=Button(frame2,text="Guardar",command=self.fGuardar,bg="spring green")
        self.btnGuardar.place(x=10,y=210,width=60,height=30)
        self.btnCancelar=Button(frame2,text="Cancelar",command=self.fCancelar,bg="orange red",relief='ridge')
        self.btnCancelar.place(x=80,y=210,width=60,height=30)

        frame3 = Frame(self, bg="#d3dde3")
        frame3.place(x=247,y=0,width=420,height=259)

        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4"))
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60,anchor=CENTER)
        self.grid.column("col2",width=90,anchor=CENTER)
        self.grid.column("col3",width=90,anchor=CENTER)
        self.grid.column("col4",width=90,anchor=CENTER)

        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Codigo", anchor=CENTER)
        self.grid.heading("col2", text="Producto", anchor=CENTER)
        self.grid.heading("col3", text="Grupo", anchor=CENTER)
        self.grid.heading("col4", text="Precio", anchor=CENTER)

        self.grid.pack(side=LEFT)

        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT,fill=Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode'] ='browse'
        
