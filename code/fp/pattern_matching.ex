foo = {1, 2.4, 3.1}
case foo do
  {1, 2, 3} ->
    IO.puts("it's a list with 1, 2, and 3")
  {1, 2, _} ->
    IO.puts("it's a list with 1, 2, and whatever")
  {1, x, y} when is_float(x) and is_float(y) ->
    IO.puts("it's a list with 1, and two floats")
  _ ->
    "whatever"
end
