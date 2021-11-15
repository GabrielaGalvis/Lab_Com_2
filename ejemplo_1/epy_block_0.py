import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  


	def __init__(self,):  
		"""Bloque acumulador simplemente toma la senal entrante y entrega una senal acumulada"""
		gr.sync_block.__init__( 
		self,
		name='Acumulador',
		in_sig=[np.float32],
		out_sig=[np.float32]
		)
		self.acum_anterior=0

	def work(self, input_items, output_items):
		x=input_items[0]
		y=output_items[0]
		N=len(x)
		y[:]=self.acum_anterior+np.cumsum(x)#se usa esto debido a que se quiere saber el acumulado de toda 			#la señal no solo el de un vector
		self.acum_anterior=y[N-1]
		return len(x)

      
