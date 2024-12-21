"use client";

import { useForm } from "react-hook-form";
import { Form, FormControl, FormField, FormItem } from "../ui/form";
import { Button } from "../ui/button";
import { ExternalLink, SendHorizontal, X } from "lucide-react";
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
import { TextGenerateEffect } from "../ui/text-generate-effect";
import { ScrollArea } from "../ui/scroll-area";

import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer";
import Image from "next/image";
import { Separator } from "../ui/separator";
import Link from "next/link";

type DataType = {
  value: string;
  selectValue: String;
  language: "fr" | "en";
};

type responseType = {
  is_error: boolean;
  message: string;
  bayt: string;
};

export function MainForm() {
  const { toast } = useToast();
  const [value, setValue] = useState("1");
  const [isTranslationVisible, setIsTranslationVisible] =
    useState<boolean>(false);
  const [translationContent, setTranslationContent] = useState<string>("");
  const [showAnimation, setShowAnimation] = useState(false);

  useEffect(() => {
    const isTranslation = value === "2";
    setIsTranslationVisible(isTranslation);
    if (!isTranslation) {
      setShowAnimation(false);
      setTranslationContent("");
    }
  }, [value]);

  const form = useForm<DataType>({
    defaultValues: {
      value: "",
      selectValue: "1",
      language: "en",
    },
  });

  async function onSubmit(input: DataType) {
    const value = input.value;
    const selectValue = input.selectValue;
    const language = input.language;
    const URL = getURL();

    switch (selectValue) {
      case "1":
        const { data }: { data: responseType } = await axios.post(
          `${URL}/py/verify_input`,
          {
            proverb_input: value,
          }
        );

        if (data.is_error) {
          toast({
            title: data.message,
            description: `Found in: ${data.bayt}`,
            variant: "destructive",
          });
        } else {
          toast({
            title: data.message,
            description: data.bayt,
            variant: "default",
          });
        }
        break;
      case "2":
        try {
          const { data } = await axios.post(`${URL}/py/translation`, {
            input: value,
            translate_to: language,
          });
          if(data.is_error){
            toast({
              title: data.translation,
              variant: "destructive",
              description: `Found: ${data.bayt}`
            })
          }
          else{
            setTranslationContent(data.translation);
            setShowAnimation(false);
            requestAnimationFrame(() => setShowAnimation(true));
          }
        } catch (e) {
          toast({
            title: `${e}`,
            variant: "destructive",
          });
        }
        break;
      default:
        console.log("Hello World");
    }
  }

  return (
    <div className="max-w-[30rem] w-full flex flex-col gap-4">
      <Form {...form}>
        <form
          onSubmit={form.handleSubmit(onSubmit)}
          className="flex items-center gap-2 flex-col w-full"
        >
          <FormField
            control={form.control}
            name="value"
            render={({ field }) => (
              <FormItem className="w-full">
                <FormControl>
                    <Textarea rows={6} placeholder="Anything in your mind?" {...field} />                  
                </FormControl>
              </FormItem>
            )}
          />

          <div className="flex w-full gap-2">
            <FormField
              control={form.control}
              name="selectValue"
              render={({ field }) => (
                <FormItem className="w-full">
                  <Select
                    onValueChange={(e) => {
                      field.onChange(e);
                      setValue(e);
                    }}
                    value={value}
                  >
                    <FormControl>
                      <SelectTrigger className="w-full">
                        <SelectValue placeholder="Compiler" />
                      </SelectTrigger>
                    </FormControl>
                    <SelectContent>
                      <SelectItem value="1">Compiler</SelectItem>
                      <SelectItem value="2">Translator</SelectItem>
                      <SelectItem value="3">Suggestions</SelectItem>
                    </SelectContent>
                  </Select>
                </FormItem>
              )}
            />

            {isTranslationVisible && (
              <FormField
                control={form.control}
                name="language"
                render={({ field }) => (
                  <FormItem className="w-full">
                    <Select
                      onValueChange={field.onChange}
                      defaultValue={String(field.value)}
                    >
                      <FormControl>
                        <SelectTrigger className="w-full">
                          <SelectValue placeholder="English" />
                        </SelectTrigger>
                      </FormControl>
                      <SelectContent>
                        <SelectItem value="en">English</SelectItem>
                        <SelectItem value="fr">French</SelectItem>
                      </SelectContent>
                    </Select>
                  </FormItem>
                )}
              />
            )}
            <Button type="submit">
              <SendHorizontal />
            </Button>
          </div>
        </form>
      </Form>

      <Drawer>
        <DrawerTrigger className="text-muted-foreground text-sm underline hover:text-white/75 duration-200">
          Show more information
        </DrawerTrigger>
        <DrawerContent className="min-h-[75%]">
          <DrawerHeader>
            <DrawerTitle>
              Abu at-Tayyib Ahmad ibn al-Husayn al-Mutanabbi al-Kindi
            </DrawerTitle>
            <DrawerDescription>Abbasid poet</DrawerDescription>
          </DrawerHeader>
          <DrawerClose className="absolute right-4 top-4">
            <Button variant="ghost">
              <X />
            </Button>
          </DrawerClose>

          <div className="size-full px-24 flex gap-6 mt-8">
            <div className="w-1/5 aspect-[1/1.21] rounded-xl bg-white overflow-hidden">
              <Image
                src="/moutanabi.jpg"
                width={1000}
                height={1000}
                alt="moutanabi image"
              />
            </div>
            <div className="w-2/5">
              <p className="text-black/95 dark:text-white/95">
                <span className="min-w-12 inline-block">
                  Born:
                </span>
                <span className="text-muted-foreground">Kufa, Iraq</span>
              </p>
              <p className="text-black/95 dark:text-white/95">
                <span className="min-w-12 inline-block">
                  Died:
                </span>
                <span className="text-muted-foreground">
                  September 23, 965 AD, Numaniyah, Iraq
                </span>
              </p>
              <p className="text-black/95 dark:text-white/95">
                <span className="min-w-12 inline-block">
                  Era:
                </span>
                <span className="text-muted-foreground">
                  Islamic Golden Age
                </span>
              </p>
                <Separator className="my-4"/>
              <div>
                <p>
                  <span className="text-muted-foreground">
                Abū al-Ṭayyib Aḥmad ibn al-Ḥusayn al-Mutanabbī al-Kindī from Kufa, Abbasid Caliphate, was a famous Abbasid-era Arabian poet at the court of the Hamdanid emir Sayf al-Dawla in Aleppo, and for whom he composed 300 folios of poetry. 
                  </span>
                <Link href="https://en.wikipedia.org/wiki/Al-Mutanabbi" target="_blank" className="text-blue-400">
                  <ExternalLink className="w-4 pb-1 ml-1 inline"/>
                </Link>
                </p>
                
              </div>

            </div>
              <div className="w-2/5 rounded-xl">
                <iframe src="https://www.youtube.com/embed/SWgu48f2rxk" allowFullScreen  className="w-full aspect-video"></iframe>
              </div>
          </div>
        </DrawerContent>
      </Drawer>

      {isTranslationVisible && showAnimation && translationContent && (
        <div className="mt-4 absolute right-4 top-12 h-[90vh] w-[30%] border-white/15 border rounded-xl p-4 bg-[#121212]">
          <ScrollArea className="w-full h-full">
            <TextGenerateEffect
              duration={2}
              filter={false}
              words={translationContent}
            />
          </ScrollArea>
        </div>
      )}
    </div>
  );
}
