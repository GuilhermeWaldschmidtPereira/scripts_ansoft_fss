function funcao_add_1!(v)
    for i in 1:length(v)
        v[i] += 1
    end

    return nothing
end

v = [10,11,12]
funcao_add_1!(v)
v