if(field.type==="select"){

return(

<TextField
select
fullWidth
size="small"
label={field.label}
name={field.name}
value={value}
onChange={onChange}
>

{field.options?.map(option=>(

<MenuItem
key={option}
value={option}
>
{option}
</MenuItem>

))}

</TextField>

);

}

return(

<TextField
fullWidth
size="small"
type={field.type}
label={field.label}
name={field.name}
value={value}
onChange={onChange}
/>

);