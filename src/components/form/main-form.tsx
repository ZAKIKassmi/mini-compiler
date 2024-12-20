"use client";

import { useForm } from "react-hook-form";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
} from "../ui/form";
import { Input } from "../ui/input";
import { Button } from "../ui/button";
import { Mic , SendHorizontal, X} from 'lucide-react';

import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../ui/select";


import { getURL } from "@/utils/getURL";
import axios from "axios";
import { useToast } from "@/hooks/use-toast";
import { useEffect, useState } from "react";
import { Textarea } from "../ui/textarea";

type DataType = {
  value: string;
  selectValue: String;
};


type responseType = {

    is_error:boolean;
    message: string;
    bayt: string;

}

export function MainForm() {
  const {toast} = useToast();
  const [isTextArea, setIsTextArea] = useState(false);

  const form = useForm<DataType>({
    defaultValues: {
      value: "",
    },
  });

  async function onSubmit(input: DataType) {
    const value = input.value;
    const URL = getURL();
    const {data}:{data:responseType} = await axios.post(`${URL}/py/verify_input`,{
    proverb_input: value,
    is_textarea: isTextArea
    });
    
    if(data.is_error){
      toast({
        title: data.message,
        variant: "destructive"
      });
    }
    else{
      toast({
        title: data.message,
        variant: "default"
      });
    }
  }



  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="max-w-[30rem] w-full flex items-center gap-2 flex-col"
      >
        <div className="flex w-full gap-2">

        <FormField
          control={form.control}
          name="value"
          render={({ field }) => (
            <FormItem className="w-full">
              <FormControl>
                {
                  isTextArea ? 
                  
                  <Textarea placeholder="Anything in your mind?" {...field}/>
                  :
                  <Input placeholder="Anything in your mind?" {...field} />
                }
              </FormControl>
            </FormItem>
          )}
          />
          <Button  type="button" onClick={()=>setIsTextArea(!isTextArea)}>
            {
              isTextArea ? "One line" : "Multiple lines"
            }
          </Button>
        </div>
        <div className="flex w-full gap-2">
          <FormField
            control={form.control}
            name="selectValue"
            render={({ field }) => (
              <FormItem className="w-full ">
                <FormControl>
                  <Select>
                    <SelectTrigger className="w-full">
                      <SelectValue placeholder="Compiler" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem defaultChecked value="1">
                        Compiler
                      </SelectItem>
                      <SelectItem value="2">Translator</SelectItem>
                      <SelectItem value="3">Suggestions</SelectItem>
                    </SelectContent>
                  </Select>
                </FormControl>
              </FormItem>
            )}
          />
        
          <Button type="submit">
              <SendHorizontal/>
          </Button>
           
          
        </div>
      </form>
    </Form>
  );
}
