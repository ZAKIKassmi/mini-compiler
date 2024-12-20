"use client";

import { useForm } from "react-hook-form";
import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel } from "../ui/form";
import { Input } from "../ui/input";
import { Button } from "../ui/button";


type DataType = {
  value: string;
}

export function MainForm(){

  const form = useForm<DataType>({
    defaultValues: {
      value: ""
    }
  });


  function onSubmit(data: DataType){
      const value = data.value;
      console.log(value);
  }

  return(
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="max-w-[30rem]">
          <FormField
            control={form.control}
            name="value"
            render={
              ({field}) => (
                <FormItem>
                  <FormLabel>Poetry</FormLabel>
                  <FormControl>
                    <Input placeholder="Anything in your mind?" {...field}/>
                  </FormControl>
                  <FormDescription>
                    Feel free to change this into a textare for large inputs
                  </FormDescription>
                </FormItem>
              )
            } 
          
          />
            
          <Button type="submit">
            Submit 
          </Button>
      </form>
    </Form>
  );
}