// Code your design here
`timescale 1ns/1ps

module memory (
    input   wire                  clk,  
    input   wire [7:0] address,    
    input   wire [7:0] write_data, 
    input   wire                  cs,       
    input   wire                  we,         
    input   wire                  oe,          
	output  reg [7:0]  read_data, 
	inout IO_pin
  ); 
  
    

endmodule 

