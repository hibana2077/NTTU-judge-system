num = gets.chomp.to_i

for i in 1..num
    nums = gets.chomp.split.map(&:to_i)
    sum = nums.sum
    puts "#{sum}"
end
