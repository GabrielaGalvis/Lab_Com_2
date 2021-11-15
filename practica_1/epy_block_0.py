import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  


	def __init__(self,):  
		"""Bloque promediador"""
		gr.sync_block.__init__( 
		self,
		name='Time average',
		in_sig=[np.float32],
		out_sig=[np.float32,np.float32,np.float32,np.float32,np.float32]
		)
		self.acum_anterior=0
		self.Ntotales=0
		#self.acum_cuad=0
		#self.acum_des=0
		self.acum_anterior2=0
		self.acum_anterior3=0

	def work(self, input_items, output_items):
		x=input_items[0]
		y1=output_items[0]#media
		y2=output_items[1]#media cuadratica
		y3=output_items[2]#RMS
		y4=output_items[3]#Potencia promedio
		y5=output_items[4]#Desviacion estandar
		
		N=len(x)
		self.Ntotales=self.Ntotales+N
		acumulado=self.acum_anterior+np.cumsum(x)#se usa esto debido a que se quiere saber el acumulado de toda 			#la señal no solo el de un vector
		self.acum_anterior=acumulado[N-1]
		y1[:]=acumulado/self.Ntotales
		
		#media cuadratica
		
		x2=np.multiply(x,x)
		acumulado2=self.acum_anterior2+np.cumsum(x2)#se usa esto debido a que se quiere saber el acumulado de toda 			#la señal no solo el de un vector
		self.acum_anterior2=acumulado2[N-1]
		y2[:]=acumulado2/self.Ntotales
		
		#RMS
		
		y3[:]=np.sqrt(y2)
		
		#Potencia promedio
		
		y4[:]=np.multiply(y3,y3)
		
		#Desviación estandar
		
		x3=np.multiply(x-y1,x-y1)
		acumulado3=self.acum_anterior3+np.cumsum(x3)#se usa esto debido a que se quiere saber el acumulado de toda 			#la señal no solo el de un vector
		self.acum_anterior3=acumulado3[N-1]
		y5[:]=np.sqrt(acumulado3/self.Ntotales)	
	 

		
		return len(x)

      
