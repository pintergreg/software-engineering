defmodule Darkvision do
    @spec power(integer(), integer()) :: integer()
    def power(a, b) do
        if b > 1 do
            a * power(a, b - 1)
        else
            a
        end
    end
    @spec what_to_do(integer(), integer(), function()) :: integer()
    def what_to_do(a, b, func) do
        func.(a, b)
    end
end

IO.puts(Darkvision.power(3, 4))

IO.puts(Darkvision.what_to_do(3, 4, &Darkvision.power/2))
IO.puts(Darkvision.what_to_do(3, 4, fn x, y -> x + y end))
sub = fn x, y -> x - y end
IO.puts(Darkvision.what_to_do(3, 4, sub))
