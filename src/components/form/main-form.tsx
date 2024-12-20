"use client";

import { useForm } from "react-hook-form";
import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel } from "../ui/form";
import { Input } from "../ui/input";
import { Button } from "../ui/button";
import { useToast } from "@/hooks/use-toast";

type DataType = {
  value: string;
}

export function MainForm(){
  const {toast} = useToast();

  const form = useForm<DataType>({
    defaultValues: {
      value: ""
    }
  });


  function onSubmit(data: DataType){
      toast({
          title: data.value,
          description: "Any thing went wrong?",
          duration: 1500
      });
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