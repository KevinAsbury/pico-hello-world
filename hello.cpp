// #include <stdio.h> // uncomment for printf
#include <iostream> // uncomment for std::cout
#include "pico/stdlib.h"

int main()
{
  stdio_init_all();
  while (true)
  {
    // Testing to see if both of these work (they do)
    std::cout << "Hello, world!\n";
    // printf("Hello, world!\n");
    sleep_ms(1000);
  }
  return 0;
}