`include "calc.v"
`include "calc_dsp.v"

module top( input CLK, output LED_R, output LED_G, output LED_B);

   wire correct;

   //implementation without DSP
   // calc calc_inst(
   //    .clk(CLK), .correct(correct)
   // );

   //implementation with DSP
   calc_dsp calc_dsp_inst(
      .clk(CLK), .correct(correct)
   );

  //leds are active low
  assign LED_R = ~correct;
  assign LED_G = ~correct;
  assign LED_B = ~correct;

  initial begin
  end

  always @(posedge CLK)
  begin
  end

endmodule
