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


import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer";

type DataType = {
  value: string;
  selectValue: String;
};

export function MainForm() {

  const form = useForm<DataType>({
    defaultValues: {
      value: "",
    },
  });

  function onSubmit(data: DataType) {}

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
                <Input placeholder="Anything in your mind?" {...field} />
              </FormControl>
            </FormItem>
          )}
          />
          <Button type="submit"><Mic/></Button>
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
          <Drawer>
          <Button type="submit" asChild>
            <DrawerTrigger>
              <SendHorizontal/>
            </DrawerTrigger>
          </Button>
            <DrawerContent >
              <DrawerHeader>
                <DrawerTitle>Did you know this?</DrawerTitle>
              </DrawerHeader>
              
              <DrawerFooter>
                <DrawerClose>
                  <Button variant="ghost" className="absolute top-4 right-4"><X/></Button>
                </DrawerClose>
              </DrawerFooter>
            </DrawerContent>
          </Drawer>
          
        </div>
      </form>
    </Form>
  );
}
